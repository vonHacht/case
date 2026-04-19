select
    type_id,
    type_name
from {{ ref('stg_type') }}