# Indoctrination — Voxel World Design Document

## Visión General

Mundo abierto 2D basado en cuadrícula de voxels (estilo Terraria) con destrucción física avanzada.
El mundo está compuesto por tiles destructibles en una cuadrícula. Cada tile tiene un material
con HP, modo de daño, y propiedades de debris.

## Sistema de Materiales

### Tipos Básicos
- **Base**: Terreno (Tierra, Arena, BedRock)
- **Mixed**: Terreno O construcción (Cemento, Ladrillo, Metal)
- **Layer**: Recubrimiento (Pintura)

### Modos de Daño
- **Additive**: Siempre resta daño
- **Restrictive**: Inmune a golpes débiles

## Armas Base

| Arma | Daño | Velocidad | Especial |
|------|------|-----------|----------|
| Pistola | 15 | 5/s | Semi-auto |
| Rifle | 25 | 10/s | Full-auto |
| RPG | 80 | 1/s | Explosión |
| Granada | 60 | 0.8/s | Arco parabólico |

## Arquitectura Técnica

- **Player**: MonoBehaviour (Interacción compleja)
- **World Grid**: NativeArray (Cache-friendly)
- **Debris**: ECS + Physics (Escalar a 10k+ partículas)
- **Damage**: Burst Jobs (Paralelizar explosiones)

---

Ver documentación completa para detalles de implementación.
