import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../context';

export const Header = () => {
  const authContext = useContext(AuthContext);
  return (
    <nav>
      <ul>
        <li style={{display: 'inline'}}>
          <Link to="/">Login </Link>
        </li>
        <li style={{display: 'inline'}}>
          <Link to="/tickets">Tickets </Link>
        </li>
        <li style={{display: 'inline'}}>
          <Link to="/tickets/new">New ticket </Link>
        </li>
        <li style={{display: 'inline'}}>
          <Link to="/users">Users</Link>
        </li>
        <li style={{padding:100}}>
          <button onClick={authContext.logout}>Logout</button>
        </li>
      </ul>
    </nav>
  );
}
