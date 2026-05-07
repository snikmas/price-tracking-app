from datetime import datetime

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from ...domain.enums import Country, Currency, Gender

# base is a table
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    nickname: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    gender: Mapped[Gender | None] = mapped_column(SqlEnum(Gender), nullable=True)
    country: Mapped[Country | None] = mapped_column(SqlEnum(Country), nullable=True)
    email: Mapped[str | None] = mapped_column(String(50), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    currency: Mapped[Currency] = mapped_column(SqlEnum(Currency), default=Currency.USD)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    notifications: Mapped["UserNotifications | None"] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"<User id={self.id!r} nickname={self.nickname!r}>"


class UserNotifications(Base):
    __tablename__ = "user_notifications"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    email_notifications: Mapped[bool] = mapped_column(default=True)
    phone_notifications: Mapped[bool] = mapped_column(default=True)
    notify_if_higher_price: Mapped[bool] = mapped_column(default=True)
    notify_if_lower_price: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped[User] = relationship(back_populates="notifications")

    def __repr__(self) -> str:
        return f"<UserNotifications user_id={self.user_id!r}>"
