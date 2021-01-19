import { Ticket } from '../models/Ticket';
import { TicketRow } from './TicketRow'

interface Props {
  tickets: Ticket[];
}

export const TicketList = ({tickets}: Props) => {
  return (
    <ul>
      {tickets.map(ticket =>
        <li key={ticket.id}>
          <TicketRow ticket={ticket}/>
        </li>
      )}
    </ul>
  );
}
