import React, { useEffect, useState } from "react";
import {
  Redirect,
  Route,
  Switch,
  useLocation
} from "react-router-dom";
import { TicketFilterableList } from './components/TicketFilterableList'
import { Header } from './components/Header'
import { Login } from './components/Login'
import { CreateTicket } from './components/CreateTicket'
import { PreviewTicket } from './components/PreviewTicket'
import { AuthContext } from './context'
import { getToken } from './actions'
import './App.css';


export default function App() {
  const [token, setToken] = useState<string>();

  const login = async (username: string, password: string) => {
    const token = await getToken(username, password);
    setToken(token);
    if (!!token) {
      localStorage.setItem(
        'userData',
        token
      );
    }
  }

  const logout = () => {
    setToken(undefined);
    localStorage.removeItem('userData');
  }

  useEffect(() => {
    const token = localStorage.getItem('userData');
    if (!!token) {
      setToken(token);
    }
  }, []);

  const { pathname } = useLocation();
  return(
    <>
    <AuthContext.Provider
      value={{
        isLoggedIn: !!token,
        token: token,
        login: login,
        logout: logout
      }}
    >
      <div>
        <Header />
        <p>logged in: {(!!token).toString()}</p>
        <Switch>
          <Redirect from="/:url*(/+)" to={pathname.slice(0, -1)} />
          <Route path="/tickets/new" component={CreateTicket}/>
          <Route path="/tickets/:id" component={PreviewTicket}/>
          <Route path="/users" component={Users}/>
          <Route path="/tickets" component={TicketFilterableList}/>
          <Route exact path="/" component={Login}/>
        </Switch>
      </div>
    </AuthContext.Provider>
    </>
  );
}

function Users() {
  return <h2>Users</h2>;
}
