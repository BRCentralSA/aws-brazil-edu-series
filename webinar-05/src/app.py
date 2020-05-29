from src.flask_config import FlaskConfs


def main():
    """Main function"""
    flask_configs = FlaskConfs()

    # Running flask application server
    flask_configs.run_app()


if __name__ == "__main__":
    main()
