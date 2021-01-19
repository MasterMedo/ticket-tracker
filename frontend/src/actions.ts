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
}

export const getCategories = async () => {
  return fetch("/categories")
    .then(r => r.json());
}

export const deleteTicket = (ticket_id: number) => {
  fetch(`/tickets/${ticket_id}`, {
    method: "delete",
  });
}

export const getTicket = (ticket_id: number) => {
  return fetch(`/tickets/${ticket_id}`)
    .then(r => r.json());
}
