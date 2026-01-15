import click
from app.Seeders.user_seeder import seed_users
from flask.cli import with_appcontext

@click.command("seed")
@with_appcontext
def seed():
    try:
        result = seed_users()

        if result is True:
            click.echo("✅ Database seeded successfully")
        elif result is False:
            click.echo("⚠ Users already exist. Skipping seeding.")

    except Exception as e:
        click.echo(f"❌ Seeding failed: {e}")
