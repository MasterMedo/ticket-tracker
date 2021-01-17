import { Category } from '../models/Category';
import { TicketList } from './TicketList'
import { useEffect, useState } from 'react';
import { Link } from "react-router-dom";


export const TicketFilterableList = () => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<Category>();

  useEffect (() => {
    fetch("/categories").then(r => r.json()
      .then((data: Category[]) => {
        setCategories(data);
      }));
  }, []);

  return (
    <div>
      <ul>
        {categories.map(category =>
        <li style={{display: 'inline'}} onClick={() => setSelectedCategory(category)}>
            <Link to={"/tickets?name=" + category.name}>{category.name} </Link>
          </li>
        )}
      </ul>
      <TicketList category={selectedCategory?.name || ""}/>
    </div>
  );
}
