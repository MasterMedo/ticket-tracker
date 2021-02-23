import moment from 'moment';
import { useHistory } from 'react-router-dom';
import {Ticket} from '../models/Ticket';
import { deleteTicket } from '../actions';

interface Props {
  ticket: Ticket;
}

export const TicketRow = ({ticket}: Props) => {
  let history = useHistory();

  const answered = ticket.answered ?
  <span style={{color: 'red'}}>CLOSED</span> :
  <span style={{color: 'green'}}>OPEN</span>;
  return (
    <div className="flex-d box-row flex-auto min-width-0 position-relative border rounded-2 m-2">
      <div className="flex-auto min-width-0 p-0">
        <a className="v-align-middle h4"
            href={`tickets/${ticket.id}`}>
          {ticket.title}
        </a>
        <div className="text-small text-grey">
          <span>
            #{ticket.id} opened
            <time title={ticket.timestamp} className=""
                  dateTime={ticket.timestamp}>
                {" " + moment.utc(ticket.timestamp).fromNow()}
            </time> by
            <a href="...">
                {" " + ticket.submitter_id}
            </a>
          </span>
        </div>
        <div>
          <span>{answered}</span>
        </div>
        <button onClick={() => {
          deleteTicket(ticket.id);
        }}>delete</button>
      </div>
    </div>
  );
}
