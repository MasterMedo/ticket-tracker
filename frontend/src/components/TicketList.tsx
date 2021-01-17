import { Ticket } from '../models/Ticket';
import { TicketRow } from './TicketRow'
import { useEffect, useState } from 'react';

interface Props {
  category: string;
}

export const TicketList = ({category}: Props) => {
  const [tickets, setTickets] = useState<Ticket[]>([]);
  useEffect (() => {
    fetch("/tickets/" + category).then(r => r.json()
      .then((data: Ticket[]) => {
        setTickets(data.sort((a, b) => a.timestamp < b.timestamp ? 1 : -1))
      }));
  }, []);

  return (
    <ul>
      {tickets.map(ticket =>
        <li>
          <TicketRow ticket={ticket}/>
        </li>
      )}
    </ul>
  );
}
