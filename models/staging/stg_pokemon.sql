select
    cast(pokemon_id as integer) as pokemon_id,
    pokemon_name,
    cast(height as integer) as height,
    cast(weight as integer) as weight,
    cast(base_experience as integer) as base_experience,
    cast(species_id as integer) as species_id,
    species_name
from {{ ref('raw_pokemon') }}