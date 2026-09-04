from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DiagnosticRecord(Base):
    __tablename__ = "diagnostic_records"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=False, index=True)  # Logical Tenant Isolation
    original_text = Column(Text, nullable=False)
    corrected_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())