


## Key Features

-   **Views:** Create custom views which is a combination of filters, sort and columns.
    -   **Pinned View:** Pin important leads and deals in the sidebar.
    -   **Public View:** Share views with all users.
    -   **Saved View:** Save views for later use.
-   **Email Communication:** Send and receive emails directly from the Lead/Deal Page.
-   **Email Templates:** Create and use email templates for faster communication.
-   **Comments:** Add comments to leads and deals to keep track of the conversation.
-   **Notifications:** Get notified when someone mentions you in a comment.
-   **Service Level Agreement:** Set SLA for leads and deals and get notified when the SLA is breached.
-   **Assignment Rule:** Automatically assign leads and deals to users based on the criteria.
-   **Tasks:** Create tasks for leads and deals.
-   **Notes:** Add notes to leads and deals.
-   **Call Logs:** See the call logs with call details and recordings.

## Integrations

-   **Twilio:** Integrate Twilio to make and receive calls from the CRM. You can also record calls. It is a built-in integration.
-   **WhatsApp:** Integrate WhatsApp to send and receive messages from the CRM. [Westronet WhatsApp](https://github.com/shridarpatil/frappe_whatsapp) is used for this integration.

## Getting Started



### Local Setup

1. [Install Bench](https://github.com/frappe/bench).
2. Install Westro  CRM app:
    ```sh
    $ bench get-app https://github.com/westronet/westrocrm.git
    ```
3. Create a site with the crm app:
    ```sh
    $ bench --site sitename.localhost install-app westrocrm
    ```
4. Open the site in the browser:
    ```sh
    $ bench browse sitename.localhost --user Administrator
    ```
5. Access the crm page at `sitename.localhost:8000/crm` in your web browser.

## Need help?

Join our [telegram group](https://t.me/frappecrm) for instant help.

## Documentation

Check out the [official documentation](https://docs.frappe.io/crm) for more details.

## License

[GNU Affero General Public License v3.0](LICENSE)
