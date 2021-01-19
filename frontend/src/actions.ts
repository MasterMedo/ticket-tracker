import { Auth } from './models/Auth'

export const getToken = (username: string, password: string) => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username,
        password: password,
      })
    }
    return fetch("/auth", requestOptions)
      .then(r => r.json())
      .then((data: Auth) => data.access_token);
  };
