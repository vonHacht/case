select
    cast(pokemon_id as integer) as pokemon_id,
    cast(type_id as integer) as type_id,
    cast(type_slot as integer) as type_slot
from {{ ref('raw_pokemon_type') }}