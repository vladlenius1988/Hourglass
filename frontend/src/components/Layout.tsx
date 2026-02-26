import React from "react";
import type { ReactNode } from 'react';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="app-container">
      <header className="app-header">
        <nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/login">Login</a></li>
    <li><a href="/register">Register</a></li>
  </ul>
</nav>
      </header>

      <main className="app-main">
        {children}
      </main>

      <footer className="app-footer">
        <p>&copy; 2026 Hourglass Project</p>
      </footer>
    </div>
  );
};

export default Layout;