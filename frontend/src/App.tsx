import React from "react";
import {
  BrowserRouter as Router,
  RouteComponentProps,
  Switch,
  Route,
  Link,
  useParams
} from "react-router-dom";
import { TicketList } from './components/TicketList'
import { CreateTicket } from './components/CreateTicket'
import './App.css';

export default function App() {
  return(
    <Router>
      <div>
        <nav>
          <ul>
            <li style={{display: 'inline'}}>
              <Link to="/">Home </Link>
            </li>
            <li style={{display: 'inline'}}>
              <Link to="/tickets/new">New ticket </Link>
            </li>
            <li style={{display: 'inline'}}>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/tickets/new" component={NewPost}/>
          <Route path="/tickets/:id" component={ViewTicket}/>
          <Route path="/users" component={Users}/>
          <Route path="/" component={Home}/>
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div>
      <CreateTicket/>
      <TicketList/>
    </div>
  );
}

function NewPost() {
  return <CreateTicket/>;
}

function Users() {
  return <h2>Users</h2>;
}

function ViewTicket(){
  const { id } = useParams<{id: string}>();
  return <p>{id}</p>;
}
