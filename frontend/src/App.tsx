import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { TicketFilterableList } from './components/TicketFilterableList'
import { CreateTicket } from './components/CreateTicket'
import { PreviewTicket } from './components/PreviewTicket'
import { Auth } from './models/Auth'
import './App.css';


export default function App() {
  const [token, setToken] = useState<string>('what');
  useEffect (() => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: "mastermedo",
        password: "password"
      })
    }
    fetch("/auth", requestOptions)
      .then(r => r.json())
      .then((data: Auth) => setToken(data.access_token));
  }, []);
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
          <Route path="/tickets/new" component={CreateTicket}/>
          <Route path="/tickets/:id" component={PreviewTicket}/>
          <Route path="/users" component={Users}/>
          <Route path="/" component={TicketFilterableList}/>
        </Switch>
      </div>
    </Router>
  );
}

function Users() {
  return <h2>Users</h2>;
}
