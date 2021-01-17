import { useState, useEffect } from 'react';
import { Ticket } from '../models/Ticket';
import { useParams } from 'react-router-dom';
import moment from 'moment';

interface ParamTypes {
  id: string
}

export const PreviewTicket = () => {
  const [ticket, setTicket] = useState<Ticket>({answered: false, timestamp: 'hehe', submitter_id: 3, id: 4, title: 'aouch', content: ''});
  let { id } = useParams<ParamTypes>();

  useEffect(() => {
    fetch(`/tickets/${id}`)
      .then(r => r.json())
      .then((data: Ticket) => setTicket(data));
  }, [id, ticket]);

  function deleter() {
    fetch(`/tickets/${ticket.id}`, {
      method: "delete",
    });
  }

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
        <p>
          {ticket.content}
        </p>
        <div>
          <span>{answered}</span>
        </div>
        <a onClick={deleter} href="/">delete</a>
      </div>
    </div>
  );
}
