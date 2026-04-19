select
    cast(type_id as integer) as type_id,
    type_name
from {{ ref('raw_type') }}