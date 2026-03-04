import { useState } from "react";

const Header = () => {
  const [currentDate, setCurrentDate] = useState<Date>(new Date());

  const handleNextDay = () => {
    const nextDay = new Date(currentDate);
    nextDay.setDate(currentDate.getDate() + 1);
    setCurrentDate(nextDay);
  };

  const formatDate = (date: Date): string => {
    return date.toLocaleDateString("ru-RU", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
  };

  return (
    <header className="app-header">
      <div>
        <h2>{formatDate(currentDate)}</h2>
        <button onClick={handleNextDay}>Завтра</button>
      </div>
    </header>
  );
};

export default Header;