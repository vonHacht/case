select
    pokemon_id,
    pokemon_name,
    species_id,
    species_name,
    height,
    weight,
    base_experience
from {{ ref('stg_pokemon') }}