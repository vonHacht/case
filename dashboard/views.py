from django.db import connection
from django.shortcuts import render


def run_query(sql: str):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    return [dict(zip(columns, row)) for row in rows]


def index(request):
    type_distribution = run_query("""
        select
            primary_type,
            count(*) as pokemon_count
        from public.obt_pokemon
        group by primary_type
        order by pokemon_count desc
    """)

    strongest = run_query("""
        select
            pokemon_name,
            base_experience
        from public.obt_pokemon
        order by base_experience desc nulls last
        limit 10
    """)

    avg_weight = run_query("""
        select
            primary_type,
            round(avg(weight)::numeric, 2) as avg_weight
        from public.obt_pokemon
        group by primary_type
        order by avg_weight desc
    """)

    context = {
        "type_labels": [row["primary_type"] for row in type_distribution],
        "type_counts": [row["pokemon_count"] for row in type_distribution],
        "strongest_names": [row["pokemon_name"] for row in strongest],
        "strongest_values": [row["base_experience"] for row in strongest],
        "weight_labels": [row["primary_type"] for row in avg_weight],
        "weight_values": [float(row["avg_weight"]) for row in avg_weight],
        "strongest_table": strongest,
    }
    return render(request, "dashboard/index.html", context)