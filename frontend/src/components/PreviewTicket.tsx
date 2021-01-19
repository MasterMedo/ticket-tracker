import { useState, useEffect } from 'react';
import { Ticket } from '../models/Ticket';
import { useParams, useHistory } from 'react-router-dom';
import moment from 'moment';
import { getTicket, deleteTicket } from '../actions';

interface ParamTypes {
  id: string
}

export const PreviewTicket = () => {
  const [ticket, setTicket] = useState<Ticket>();
  let id = parseInt(useParams<ParamTypes>().id);
  let history = useHistory();

  useEffect(() => {
    getTicket(id).then(data => {
      if (!!data.message) {
        history.push('/tickets');
        alert(data.message)
      } else {
        setTicket(data)
      }
    });
  }, []);

  if (!ticket) {
    return <></>
  }

  const answered = ticket.answered ?
  <span style={{color: 'red'}}>CLOSED</span> :
  <span style={{color: 'green'}}>OPEN</span>;
  return (
    <div className="flex-d box-row flex-auto min-width-0 position-relative border rounded-2 m-2">
      <div className="flex-auto min-width-0 p-0">
        <span className="v-align-middle h4">
          {ticket.title}
        </span>
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
        <p>
          {ticket.content}
        </p>
        <div>
          <span>{answered}</span>
        </div>
        <button onClick={() => {
          deleteTicket(ticket.id);
          history.push('/tickets');
        }}>delete</button>
      </div>
    </div>
  );
}
