import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean, ForeignKey, Integer, text

from service_layer.database import Base


class UserMaster(Base):
    __tablename__ = 'user_master'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    email = Column(String(320), index=True, unique=True)
    is_active = Column(Boolean, server_default='f')
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = Column(UUID)
    modified_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    modified_by = Column(UUID)

    # Relational fields


class UserSubsidiary(Base):
    __tablename__ = 'user_subsidiary'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    user_master_id = Column(UUID, ForeignKey('user_master.id'), index=True)
    subsidiary_master_id = Column(UUID, ForeignKey('subsidiary_master.id'), index=True)
    is_default_subsidiary = Column(Boolean, server_default='f')
    is_register = Column(Boolean, server_default='f')
    is_active = Column(Boolean, server_default='f')
    app_feedback_date = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    app_feedback_flag = Column(Boolean, server_default='f')
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = Column(UUID)
    modified_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    modified_by = Column(UUID)

    # Relational fields


class UsersProfileConnection(Base):
    __tablename__ = 'users_profile_connection'

    id = Column(Integer, primary_key=True, unique=True)
    user_master_id = Column(UUID, ForeignKey('user_master.id'), index=True)
    unique_profile_id = Column(UUID, index=True)
    is_active = Column(Boolean, server_default='f')
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    created_by = Column(UUID)
    modified_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    modified_by = Column(UUID)

    # Relational fields


class Users_navahack(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(320), index=True, unique=True)
    last_name = Column(String(320), index=True, unique=True)
    email = Column(String(320), index=True, unique=True)
    is_present = Column(Boolean, server_default='f')
    role = Column(Integer)
