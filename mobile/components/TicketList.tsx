import React from 'react';
import {FlatList} from 'react-native';
import {Ticket} from '../models/Ticket';
import {TicketRow} from '../components/TicketRow';

interface Props {
  tickets: Ticket[];
}
export const TicketList = ({tickets}: Props) => {
  const renderItem = ({item}: {item: Ticket}) => <TicketRow ticket={item} />;
  return (
    <FlatList
      data={tickets}
      renderItem={renderItem}
      keyExtractor={(ticket: Ticket) => ticket.id.toString()}
    />
  );
};
