# Indoctrination — Arquitectura del Sistema del Personaje Esfera

> **Última actualización:** 2026-04-03  
> **Versión:** 1.0 — Base de Movimiento con Thrusters

---

## 1. Resumen del Juego

Platformer 2D basado en física. El personaje es una **esfera que gira con inercia** (tipo rueda). Se mueve exclusivamente mediante **4 Thrusters direccionales** (WASD). Los thrusters consumen **combustible configurable**. Todo el sistema es modular, preparado para upgrades, inventario, skills y capas de movimiento futuras.

### Sistema Modular de Movimiento
- Thrusters con 4 direcciones (WASD)
- Consumo de combustible configurable
- Sistema de física avanzado con Rigidbody2D
- Capas visuales desacopladas
- Preparado para upgrades y skills futuras

---

## 2. Flujo de Datos por Frame

```
PlayerInputHandler → ThrusterController → FuelSystem
                          ↓
                   ThrusterGroup
                          ↓
                   SpherePhysics → Rigidbody2D
                          ↓
         SphereSpriteRotator, OverlayTiltController, FuelBarDisplay
```

---

## 3. Puntos de Integración Futuros

- **Health/Vida**: `SphereEntity.Kill()`
- **Upgrades**: `SphereEntity.ApplyUpgrade()`
- **Inventario**: ScriptableObjects configurables
- **Skills/Abilities**: Módulo independiente
- **Armas**: Sistema de posicionamiento
- **AI Enemies**: Reemplazar `PlayerInputHandler`

---

Ver la documentación completa de arquitectura en la rama principal.
