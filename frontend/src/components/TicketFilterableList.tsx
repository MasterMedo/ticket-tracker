import { useEffect, useState } from 'react';
import { NavLink, useLocation } from "react-router-dom";
import { TicketList } from './TicketList'
import { Ticket } from '../models/Ticket';
import { Category } from '../models/Category';

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

export const TicketFilterableList = () => {
  const [tickets, setTickets] = useState<Ticket[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [query, setQuery] = useState(useQuery());

  useEffect (() => {
    fetch("/categories")
      .then(r => r.json())
      .then((data: Category[]) => {
        setCategories(data);
      });
  }, []);

  useEffect (() => {
    fetch("/tickets?" + query.toString())
      .then(r => r.json())
      .then((data: Ticket[]) => {
        setTickets(data || []);
      });
    // eslint-disable-next-line
  }, [query.toString()]);

  return (
    <>
      <ul>
        {categories.map(category =>
        <li style={{display: 'inline'}} key={category.id}>
            <NavLink to={location => {
                let tmp = new URLSearchParams(query.toString());
                tmp.set('category', category.name);
                return ({...location, search: tmp.toString()});
              }}
              onClick={() => {
                query.set('category', category.name);
                setQuery(query);
              }}>
              {category.name + ' '}
            </NavLink>
          </li>
        )}
      </ul>
      <TicketList tickets={tickets}/>
    </>
  );
}
