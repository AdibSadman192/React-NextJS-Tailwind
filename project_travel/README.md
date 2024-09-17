This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.



## Project Structure

The `project_travel` folder is organized as follows:

```
project_travel/
├── app/
│   └── page.tsx
├── components/
├── styles/
├── public/
├── utils/
```

- **app**: Contains the main application components and pages.
    - `page.tsx`: The main page component.
- **components**: Reusable UI components used throughout the project.
- **styles**: Global styles and Tailwind CSS configurations.
- **public**: Static assets like images and fonts.
- **utils**: Utility functions and helpers.

## Components Overview

- **Header**: Renders the navigation bar and site logo.
- **Footer**: Displays the footer content with links and copyright information.
- **TravelCard**: A card component to display travel destinations with images and descriptions.
- **SearchBar**: A search input to filter travel destinations.

## How It Works

1. **Routing**: Next.js handles routing based on the file structure in the `app` directory.
2. **Styling**: Tailwind CSS is used for styling components with utility-first classes.
3. **State Management**: React's built-in state management is used to manage component states.
4. **API Integration**: Fetch travel data from an external API and display it using the `TravelCard` component.

## Development Workflow

1. **Clone the repository**: `git clone <repository-url>`
2. **Install dependencies**: `npm install`
3. **Run the development server**: `npm run dev`
4. **Open the app**: Visit [http://localhost:3000](http://localhost:3000) in your browser.


## Environment and Dependencies

### Node.js Version

Ensure you are using the latest version of Node.js. You can check your Node.js version by running:

```bash
node -v
```

### Required Packages

The project relies on the latest versions of the following React and related packages:

- **react**
- **react-dom**
- **next**
- **tailwindcss**
- **autoprefixer**
- **postcss**

You can install all dependencies by running:

```bash
npm install
```

or

```bash
yarn install
```

Make sure to keep your packages updated to avoid compatibility issues.

