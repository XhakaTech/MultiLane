# MultiLane Architecture

MultiLane is a multi-layered game development framework combining physics-based character systems with destruction-based level design.

## Core Systems

### 1. Character Movement System

Physics-based platformer using:
- **Rigidbody2D Physics**: Full 2D physics simulation
- **Thruster Controllers**: 4-directional propulsion (WASD)
- **Fuel System**: Resource management for movement
- **Modular Design**: Easily upgradeable components

**Key Components:**
- `SphereEntity`: Main character facade
- `ThrusterController`: Propulsion management
- `FuelSystem`: Resource management
- `SpherePhysics`: Physics gateway

### 2. Voxel World Destruction

Tile-based destructible world:
- **Material System**: 14+ material types with different properties
- **Damage Profiles**: Additive and Restrictive damage modes
- **Debris System**: Physics-based fragment particles
- **Performance**: ECS + Burst Jobs for 10k+ particles

**Key Systems:**
- `VoxelGrid`: World data management
- `VoxelChunk`: Tilemap and physics
- `DebrisSystem`: Fragment spawning and physics
- `WeaponSystem`: Damage application

### 3. Weapon System

Multiple weapon types:
- **Ballistic**: Pistol, Rifle (point damage)
- **Explosive**: RPG, Granada (area damage)
- **Penetrating**: PerforadorA, PerforadorB (special)

**Damage Types:**
- Bullet: Point impact
- Explosive: Radius-based
- Custom: Penetration + detonation

## Design Patterns

### Facade Pattern
`SphereEntity` provides unified access to all subsystems

### Gateway Pattern
`SpherePhysics` is the only script that touches `Rigidbody2D`

### Event-Driven Architecture
Subsystems communicate via events (e.g., `OnFuelChanged`)

### Dependency Injection
Components initialized with required dependencies

## Data Flow

```
Input → ThrusterController → FuelSystem ↘
                               ↓         → SpherePhysics → Rigidbody2D
                          ThrusterGroup ↗
                                ↓
                         Visuals (read-only)
```

## Extension Points

- **Upgrades**: `SphereEntity.ApplyUpgrade()`
- **Skills**: New modules in `Scripts/Abilities/`
- **AI**: Replace `PlayerInputHandler` with `AIInputHandler`
- **Weapons**: Extend `WeaponConfig` and `ProjectileSystem`
- **Terrain**: Add special material behaviors

## Technology Stack

- **Engine**: Unity 2022 LTS+
- **Physics**: PhysX 2D
- **Data**: ECS (Entities 1.4.5)
- **Performance**: Burst Compiler
- **Version Control**: Git

---

For detailed information, see individual documentation files in `/Docs`.
