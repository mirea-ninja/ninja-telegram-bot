from __future__ import annotations

import datetime

import sqlalchemy as db

from bot.db import db_session
from bot.models.base import BaseModel

offset = datetime.timezone(datetime.timedelta(hours=3))


class ReputationUpdate(BaseModel):
    __tablename__ = "reputation_updates"

    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(db.BigInteger)
    to_user_id = db.Column(db.BigInteger, nullable=True)
    message_id = db.Column(db.BigInteger, nullable=True)
    reputation_delta = db.Column(db.FLOAT, nullable=True)
    force_delta = db.Column(db.FLOAT, nullable=True)
    new_reputation = db.Column(db.FLOAT)
    new_force = db.Column(db.FLOAT)
    updated_at = db.Column(db.DateTime(True), default=datetime.datetime.now(offset))

    def create(self):
        with db_session() as db:
            db.add(self)
            db.commit()

    @staticmethod
    def is_user_send_rep_to_message(user_id, message_id):
        with db_session() as session:
            send = (
                session.query(ReputationUpdate)
                .filter(
                    ReputationUpdate.from_user_id == user_id,
                    ReputationUpdate.message_id == message_id,
                )
                .first()
            )

            return send is not None

    @staticmethod
    def get_history(user_id):
        with db_session() as session:
            return (
                session.query(ReputationUpdate)
                .filter(ReputationUpdate.to_user_id == user_id)
                .order_by(ReputationUpdate.updated_at.desc())
                .all()
            )


ReputationUpdate.__table__.create(checkfirst=True)
