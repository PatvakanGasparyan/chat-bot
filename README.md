# WebCalcTrackbot 💱

This is a user-friendly Telegram bot for real-time currency conversion. The bot calculates currency rates, saves the complete request history to a MySQL database, and includes a dedicated Flask web dashboard for the owner to view logs in a clean table format.

---

## 🚀 Key Features

* **Fast Calculation**: The user sends a message to the bot (e.g., `100 USD EUR`), and the bot instantly replies with the result based on fresh exchange rates.
* **History Logging**: All user actions are automatically saved into a MySQL database.
* **Web Dashboard (Admin Panel)**: A simple Flask-based website that displays a table containing all past conversions.
* **Automated CI/CD**: Fully integrated with GitHub Actions to test, build, and deploy changes seamlessly via Docker.

---

## 🏗 Project Architecture & CI/CD Flow

The diagram below shows how different parts of the application communicate, including the GitHub Actions automation:

```mermaid
graph TD;
    User[User] -->|1. Sends: 100 USD EUR| Bot[Telegram Bot]
    Bot -->|2. Requests rate| API[Currency Exchange API]
    Bot -->|3. Sends result| User
    Bot -->|4. Saves log| DB[(MySQL Database)]
    WebSite[Flask Website] -->|5. Reads history| DB
    Admin[Bot Owner] -->|6. Views table| WebSite

    subgraph CI/CD Pipeline
        Developer[Developer] -->|git push| GitHub[GitHub Repository]
        GitHub -->|Triggers| Actions[GitHub Actions]
        Actions -->|Builds & Deploys| Docker[Docker Container on EC2 Server]
    end
