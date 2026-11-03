# Solid.js + Vite Quickstart Guide

This guide will walk you through the process of setting up a new [Solid.js](https://www.solidjs.com/) project using [Vite](https://vitejs.dev/) as the build tool.

Vite provides a lightning-fast development experience, and Solid.js offers a reactive, unopinionated framework for building user interfaces. This guide includes instructions for both **Node.js** (npm/yarn/pnpm) and **Bun** environments.

## 📋 Prerequisites

Before you begin, ensure you have one of the following installed on your system:

* **Node.js**: Version 18.0.0 or higher. You can download it from [nodejs.org](https://nodejs.org/).

* **Bun**: A fast all-in-one JavaScript runtime. You can install it from [bun.sh](https://bun.sh/).

## 🚀 Option 1: Setup with Node.js (npm / pnpm / yarn)

If you are using a traditional Node.js environment, follow these steps to scaffold your Solid.js project.

### 1. Scaffold the Project

Open your terminal and run one of the following commands to create a new Vite project. We will name the project `my-solid-app` and use the official Solid template.

**Using npm:**

```
npm create vite@latest my-solid-app -- --template solid

```

**Using pnpm:**

```
pnpm create vite my-solid-app --template solid

```

**Using yarn:**

```
yarn create vite my-solid-app --template solid

```

*(Note: If you want to use TypeScript, change `--template solid` to `--template solid-ts`)*

### 2. Install Dependencies

Navigate into your new project directory and install the required packages.

```
cd my-solid-app
npm install   # or pnpm install, or yarn

```

### 3. Start the Development Server

Launch the Vite development server to see your app in action.

```
npm run dev   # or pnpm dev, or yarn dev

```

## 🥟 Option 2: Setup with Bun

Bun is a drop-in replacement for Node.js that includes a significantly faster package manager and bundler.

### 1. Scaffold the Project

Run the following command to scaffold the Vite project using Bun:

```
bun create vite my-solid-app --template solid

```

*(Note: For TypeScript, use `--template solid-ts`)*

### 2. Install Dependencies

Navigate to your project folder and use Bun to install the dependencies incredibly fast:

```
cd my-solid-app
bun install

```

### 3. Start the Development Server

Start the Vite development server using Bun:

```
bun run dev

```

## 📂 Project Structure Overview

Once your project is created, your directory will look something like this:

```
my-solid-app/
├── node_modules/
├── public/
│   └── vite.svg           # Static assets served at the root path
├── src/
│   ├── assets/            # Project assets (images, fonts, etc.)
│   ├── App.css            # Styles specific to the App component
│   ├── App.jsx            # The main Solid.js component
│   ├── index.css          # Global stylesheet
│   └── index.jsx          # Entry point where Solid mounts to the DOM
├── .gitignore
├── index.html             # Main HTML file serving the app
├── package.json           # Project metadata and dependencies
└── vite.config.js         # Vite configuration file (includes solid-plugin)

```

## 🛠️ Building for Production

When you are ready to deploy your application, you need to create a production-ready build.

**For Node.js (npm):**

```
npm run build

```

**For Bun:**

```
bun run build

```

This command will bundle your application and output the optimized files into a `dist/` directory, ready to be hosted on your preferred platform (Vercel, Netlify, GitHub Pages, etc.).

To preview your production build locally:

```
npm run preview  # or bun run preview

```

## 📚 Next Steps & Resources

* [Solid.js Official Documentation](https://www.solidjs.com/docs/latest)

* [Solid.js Tutorial (Interactive)](https://www.solidjs.com/tutorial)

* [Vite Documentation](https://vitejs.dev/guide/)

* [Bun Documentation](https://bun.sh/docs)