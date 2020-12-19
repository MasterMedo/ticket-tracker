import React, {FunctionComponent}  from 'react';
import moment from 'moment';
import './App.css';

function App() {
        return(<TicketList/>);
}

class TicketList extends React.Component {
  render() {
    const tickets = [
      {
        "answered": true,
        "content": "Is this even a ticket?",
        "excerpt": "post 1",
        "id": 1,
        "submitter_id": 1,
        "timestamp": "2020-12-18T16:00:52.286032",
        "title": "First Post"
      },
      {
        "answered": false,
        "content": "Is this even a ticket?",
        "excerpt": "post 2",
        "id": 2,
        "submitter_id": 1,
        "timestamp": "2020-12-19T16:00:52.286032",
        "title": "Second Post"
      }];
    console.log(tickets)
    console.log(tickets[0])
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
}

export const TicketRow: FunctionComponent<any> = ({ticket}: any) => {
  console.log(ticket)
  const answered = ticket.answered ?
  <span style={{color: 'red'}}>CLOSED</span> :
  <span style={{color: 'green'}}>OPEN</span>;
  return (
    <div className="flex-d box-row position-relative border rounded-2 m-2">
      <div className="flex-auto min-width-0 p-0">
        <a className="v-align-middle h4"
            href={"posts/" + ticket.id.toString()}>
          {ticket.title}
        </a>
        <div className="text-small text-grey">
          <span>
            #{ticket.id} opened
            <time title={ticket.timestamp} className=""
                  dateTime={ticket.timestamp}>
                {" " + moment(ticket.timestamp).fromNow()}
            </time> by
            <a href="...">
                {" " + ticket.submitter_id}
            </a>
          </span>
        </div>
        <div>
          <span>{answered}</span>
        </div>
      </div>
    </div>
  );
}

export default App;
