select
    pt.pokemon_id,
    pt.type_id,
    pt.type_slot
from {{ ref('stg_pokemon_type') }} pt