from sqlalchemy import create_engine, Column, Integer, Text, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# Modelos

class Cliente(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(Text, nullable=False)
    NIT = Column(Text)
    REEUP = Column(Text)
    ONIE = Column(Text)
    Domicilio = Column(Text)
    nro_cta_CUP = Column(Text)
    nro_cta_MLC = Column(Text)
    Telefono = Column(Text)
    email = Column(Text)

    facturas = relationship("Factura", back_populates="cliente")


class Config(Base):
    __tablename__ = "Config"

    id = Column(Integer, primary_key=True, autoincrement=True)
    porciento_cta_fiscal = Column(Integer)
    nota_terminos = Column(Text)


class Producto(Base):
    __tablename__ = "Productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(Text, nullable=False)
    Precio = Column(Text)
    Proveedor = Column(Text)
    peso = Column(Numeric)

    detalles = relationship("DetalleFactura", back_populates="producto")


class Vendedor(Base):
    __tablename__ = "Vendedores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(Text, nullable=False)
    NIT = Column(Text)
    Domicilio = Column(Text)
    nro_cta_CUP = Column(Text)
    Tarjeta_CUP = Column(Text)
    nro_cta_MLC = Column(Text)
    Tarjeta_MLC = Column(Text)
    Telefono = Column(Text)
    email = Column(Text)

    facturas = relationship("Factura", back_populates="vendedor")


class MetodoPago(Base):
    __tablename__ = "Metodos_pagos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    metodo_pago = Column(Text, nullable=False)

    facturas = relationship("Factura", back_populates="metodo_pago_rel")


class Estado(Base):
    __tablename__ = "Estados"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Estado = Column(Text, unique=True)

    facturas = relationship("Factura", back_populates="estado_rel")


class Tipo(Base):
    __tablename__ = "Tipos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_factura = Column(Text, unique=True)

    facturas = relationship("Factura", back_populates="tipo_rel")


class Tasa(Base):
    __tablename__ = "Tasas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Divisa = Column(Text, nullable=False, unique=True)
    tasa = Column(Numeric, nullable=False)


class Factura(Base):
    __tablename__ = "Facturas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_factura = Column(Text, nullable=False, unique=True)

    tipo = Column(Integer, ForeignKey("Tipos.id"))
    Vendedor = Column(Integer, ForeignKey("Vendedores.id"))
    Cliente = Column(Integer, ForeignKey("Clientes.id"))

    Fecha = Column(Text)
    Moneda = Column(Text)
    tasa_cambio = Column(Numeric)

    metodo_pago = Column(Integer, ForeignKey("Metodos_pagos.id"))
    porciento_cta_fiscal = Column(Integer)
    Estado = Column(Integer, ForeignKey("Estados.id"))

    cliente = relationship("Cliente", back_populates="facturas")
    vendedor = relationship("Vendedor", back_populates="facturas")
    tipo_rel = relationship("Tipo", back_populates="facturas")
    metodo_pago_rel = relationship("MetodoPago", back_populates="facturas")
    estado_rel = relationship("Estado", back_populates="facturas")

    detalles = relationship(
        "DetalleFactura",
        back_populates="factura",
        cascade="all, delete-orphan"
    )


class DetalleFactura(Base):
    __tablename__ = "Detalles_facturas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    factura_id = Column(Integer, ForeignKey("Facturas.id"))
    Producto_id = Column(Integer, ForeignKey("Productos.id"))
    Cantidad = Column(Integer)
    Precio_venta = Column(Numeric)

    factura = relationship("Factura", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles")

# Fin Modelos

engine = create_engine('sqlite:///facturas.db')

Session = sessionmaker(bind=engine)
session = Session()