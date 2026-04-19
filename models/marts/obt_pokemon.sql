with type_ranked as (
    select
        pt.pokemon_id,
        t.type_name,
        pt.type_slot
    from {{ ref('fct_pokemon_type') }} pt
    join {{ ref('dim_type') }} t
      on pt.type_id = t.type_id
),

type_pivot as (
    select
        pokemon_id,
        max(case when type_slot = 1 then type_name end) as primary_type,
        max(case when type_slot = 2 then type_name end) as secondary_type
    from type_ranked
    group by 1
)

select
    p.pokemon_id,
    p.pokemon_name,
    p.species_id,
    p.species_name,
    p.height,
    p.weight,
    p.base_experience,
    tp.primary_type,
    tp.secondary_type
from {{ ref('dim_pokemon') }} p
left join type_pivot tp
  on p.pokemon_id = tp.pokemon_id