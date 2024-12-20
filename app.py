from database.connection import get_db_connection
from database.setup import create_tables
from models.agent import Agent
from models.player import Player
from models.performance import Performance
from database.setup import setup


def main_menu():
    print("\n===== MAIN MENU =====")
    print("1. Add a new agent")
    print("2. Add a new player")
    print("3. Add a new performance")
    print("4. Update agent")
    print("5. Update player")
    print("6. Update performance")
    print("7. Delete agent")
    print("8. Delete player")
    print("9. Delete performance")
    print("10. List all agents")
    print("11. List all players")
    print("12. List all performances")
    print("0. Exit")
    print("=====================")


def main():
    # Ensure tables exist
    create_tables()
    setup()

    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            # Add a new agent
            agent_name = input("Enter agent's name: ")
            agent = Agent(name=agent_name)
            agent.save()
            print(f"Agent added: {agent}")

        elif choice == "2":
            # Add a new player
            player_name = input("Enter player's name: ")
            agent_id = int(input("Enter the agent ID for this player: "))
            player = Player(name=player_name, agent_id=agent_id)
            player.save()
            print(f"Player added: {player}")

        elif choice == "3":
            # Add a new performance
            player_id = int(input("Enter the player ID for this performance: "))
            goals = int(input("Enter goals scored: "))
            assists = int(input("Enter assists made: "))
            status = input("Enter performance status: ")
            performance = Performance(player_id=player_id, goals=goals, assists=assists, status=status)
            performance.save()
            print(f"Performance added: {performance}")

        elif choice == "4":
            # Update an agent
            agent_id = int(input("Enter the agent ID to update: "))
            new_name = input("Enter the new name for the agent: ")
            agent = Agent.get_by_id(agent_id)
            if agent:
                agent.name = new_name
                agent.save()
                print(f"Agent updated: {agent}")
            else:
                print(f"No agent found with ID {agent_id}.")

        elif choice == "5":
            # Update a player
            player_id = int(input("Enter the player ID to update: "))
            new_name = input("Enter the new name for the player: ")
            player = Player.get_by_id(player_id)
            if player:
                player.name = new_name
                player.save()
                print(f"Player updated: {player}")
            else:
                print(f"No player found with ID {player_id}.")

        elif choice == "6":
            # Update a performance
            performance_id = int(input("Enter the performance ID to update: "))
            goals = int(input("Enter new goals scored: "))
            assists = int(input("Enter new assists made: "))
            status = input("Enter new status: ")
            performance = Performance.get_by_id(performance_id)
            if performance:
                performance.goals = goals
                performance.assists = assists
                performance.status = status
                performance.save()
                print(f"Performance updated: {performance}")
            else:
                print(f"No performance found with ID {performance_id}.")

        elif choice == "7":
            # Delete an agent
            agent_id = int(input("Enter the agent ID to delete: "))
            Agent.delete_by_id(agent_id)
            print(f"Agent with ID {agent_id} deleted.")

        elif choice == "8":
            # Delete a player
            player_id = int(input("Enter the player ID to delete: "))
            Player.delete_by_id(player_id)
            print(f"Player with ID {player_id} deleted.")

        elif choice == "9":
            # Delete a performance
            performance_id = int(input("Enter the performance ID to delete: "))
            Performance.delete_by_id(performance_id)
            print(f"Performance with ID {performance_id} deleted.")

        elif choice == "10":
            # List all agents
            print("\nAll Agents:")
            for agent in Agent.list_all():
                print(agent)

        elif choice == "11":
            # List all players
            print("\nAll Players:")
            for player in Player.list_all():
                print(player)

        elif choice == "12":
            # List all performances
            print("\nAll Performances:")
            for performance in Performance.list_all():
                print(performance)

        elif choice == "0":
            # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
