# Pokémon Data Model

This project demonstrates a simple end-to-end data pipeline:

1. Data ingestion via Python from the PokéAPI
2. Transformation using dbt
3. Modeling into both a dimensional schema and an OBT
4. Visualising Pokemon statistics

---

## 🧱 Data Modeling Approach

### Dimensional Model

We use a classic dimensional structure:

- `dim_pokemon`: core entity table
- `dim_type`: lookup table for Pokémon types
- `fct_pokemon_type`: bridge table linking Pokémon to types

This structure supports flexible querying and reuse.

---

### One Big Table (OBT)

The `obt_pokemon` model denormalizes the data:

- Combines Pokémon attributes and type information
- Provides a simplified interface for analytics
- Reduces need for joins in downstream queries

---

## 🎯 Use Cases

This dataset can be used to answer questions such as:

- Which Pokémon types are most common?
- Do certain types have higher average base experience?
- What are the heaviest or strongest Pokémon?

---

## 🧠 Design Tradeoffs

- Dimensional model provides flexibility and normalization
- OBT provides simplicity and ease of use

In practice, both are useful depending on the use case.

## Start

[-->](docs/start.md)