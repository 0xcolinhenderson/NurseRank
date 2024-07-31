from flask_login import UserMixin
from sqlalchemy import (
    Integer,
    Column,
    Text,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship
from app import db_manager

Base = db_manager.base

class Account(Base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    users = relationship("User", back_populates="account")

class Role(Base):
    __tablename__ = "roles"
    role_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Role {self.name}>"

class UserRole(Base):
    __tablename__ = "users_x_roles"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.role_id"), primary_key=True)
    assigned_at = Column(DateTime, nullable=False, server_default=func.now())

class User(UserMixin, Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    confirmed = Column(Boolean, nullable=False, server_default="false")
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
    account = relationship("Account", back_populates="users")
    nurse_id = Column(Integer, ForeignKey("nurses.id"), nullable=True)
    nurse = relationship("Nurse", back_populates="users", foreign_keys=[nurse_id])
    roles = relationship("Role", secondary="users_x_roles")

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return f"<User {self.email}>"
    
    def get_user_roles(self):
        return db_manager.session.query(Role.name).join(UserRole).filter(UserRole.user_id == self.user_id).all()
    
class Nurse(Base):
    __tablename__ = "nurses"
    associated_user_id= Column(Integer, ForeignKey("users.user_id"), nullable=True)
    id = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(String, unique=True)
    manager = Column(String(128), server_default="")
    department_name = Column(String(128), server_default="")
    department_id = Column(String(128), server_default="")
    rn_level = Column(String(128), server_default="N/A")
    users = relationship("User", back_populates="nurse", foreign_keys=[User.nurse_id])
