# ClimateLens: A Carbon Impact Estimator for Global Supply Chains

#### Video Demo: <[CLICK HERE](https://youtu.be/Fb3WBQ8ODUk)>
#### GitHub: [alicepigelet](https://github.com/alicepigelet)
#### edX Username: 2505_TGHO
#### Location: Saint-Gervais les Bains, France
#### Date: August 2, 2025

<img src="https://github.com/alicepigelet/Porous-Material-Energy-Project/blob/main/There%20is%20no%20planet%20B.png" alt="Alt Text" width="200" align="left" />
<br clear="all"/>

---

## Description

**ClimateLens** is a web-based platform that allows users to estimate the carbon footprint of companies and products by simulating the environmental impact across their supply chains. Through a simple interface, users can input a query (like “apple” or “Tesla”) and receive a visual breakdown of emissions across five key lifecycle stages: extraction, manufacturing, transport, packaging, and distribution.

The project was developed using **Python (Flask)** for backend routing and logic, **SQLite** for data storage, **HTML/CSS** for structure and style, and **JavaScript + Chart.js** for interactive data visualization. While current emissions values are derived from a mock dataset, the design anticipates future integration with real-world databases or APIs such as the Carbon Disclosure Project (CDP).

---

## Key Features

- **Product/Company Lookup**: Input a product name to generate an emissions profile.
- **Emissions Breakdown Chart**: Visualize emissions by lifecycle stage via a dynamic bar chart.
- **Login System** (optional): Planned functionality for users to save previous searches and compare results.
- **Extensible Architecture**: The codebase is modular and ready to integrate with live data sources in future builds.

---

## Motivation

ClimateLens was created as a final project for **CS50x**, Harvard’s Introduction to Computer Science, to demonstrate the use of programming for social good—particularly climate change mitigation through better information access. The project combines technical skills (backend web dev, database management, visualization) with a real-world problem: the opacity of carbon footprints.

This also aligns with my broader interests in **data-driven sustainability, ethical leadership, and policy-oriented tech**. I intend to include this project as part of my graduate school applications to demonstrate both my programming ability and my commitment to practical innovation.

---

## File Overview

- `app.py`: The core of the app. Routes requests, handles form input, and passes data to templates.
- `helpers.py`: Contains the `lookup_emissions` function that retrieves emissions estimates and simulates database querying logic.
- `schema.sql`: SQL script to initialize the `products` table used for basic data lookup.
- `requirements.txt`: Specifies Flask and other dependencies for setting up the environment.
- `/templates/`: HTML files:
  - `index.html`: Home page with the search form.
  - `results.html`: Displays the emissions chart.
  - `login.html`: Login form (placeholder).
- `/static/`:
  - `style.css`: CSS styles used by the templates.
  - JavaScript (inline in templates) using Chart.js for dynamic chart rendering.
- `README.md`: This file, providing complete documentation of the project.

---

## Design Decisions

### Emissions Model
Rather than relying on static values, I used a modular scoring system that assigns emission values per lifecycle stage. Each stage is represented in a dictionary (Python), and the total emissions are the sum of all stages. This simplifies future upgrades when real-time data becomes available.

### Database Structure
I chose SQLite for its simplicity and ease of setup within the CS50 environment. While currently limited to a single `products` table, it could be expanded with additional tables for users, search history, and API logs.

### Visualization
I used **Chart.js** to make the emissions data engaging and understandable for non-technical users. The bar chart updates with each query and is color-coded for clarity. This visual approach is essential when presenting sustainability data to general audiences.

### Simplicity vs Functionality
I opted to make the app functional **without requiring login**, but with a clear structure in place for future authentication features (login/register). This supports both accessibility and potential extensibility.

---

## Limitations

- Currently, emissions values are **static** and hardcoded in `helpers.py`, meaning all valid queries return the same chart unless new entries are manually added.
- The app **does not yet store user data**, history, or session logs.
- Error handling and input validation are basic and could be strengthened with future iterations.

---

## Future Extensions

- **Live API Integration**: Connect to CDP, UNFCCC, or ESG datasets for real-time emissions values.
- **Regional Factors**: Adjust estimates based on country- or region-specific carbon intensity data.
- **User Dashboards**: Let users track their searches over time and compare results.
- **Language Support**: Add multilingual support starting with French and Spanish.
- **Mobile Optimization**: Responsive redesign for mobile and tablet devices.
- **Authentication**: Enable user accounts, saved reports, and permissioned admin uploads.
