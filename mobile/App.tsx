import React, {useEffect, useState} from 'react';
import {SafeAreaView} from 'react-native';
import {TicketList} from './components/TicketList';
import {Ticket} from './models/Ticket';

const App = () => {
  const [tickets, setTickets] = useState<Ticket[]>([]);

  useEffect(() => {
    fetch('http://192.168.0.20:5000/tickets')
      .then((r) => r.json())
      .then((data: Ticket[]) => {
        setTickets(data || []);
      })
      .catch((error) => console.warn(error));
  });

  return (
    <SafeAreaView>
      <TicketList tickets={tickets} />
    </SafeAreaView>
  );
};

export default App;
