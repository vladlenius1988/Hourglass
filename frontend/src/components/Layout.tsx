import type { ReactNode } from 'react';
import Header from "./Header";

interface LayoutProps {
  children: ReactNode;
}

const Layout = ({ children }: LayoutProps) => {
  return (
    <div className="app-container">
      <Header />
      <main className="app-main">{children}</main>
      <footer className="app-footer">
        © 2026 Hourglass
      </footer>
    </div>
  );
};

export default Layout;