import React from 'react';
import { FlatList, Pressable } from 'react-native';
import { Ticket } from '../models/Ticket';
import { TicketRow } from '../components/TicketRow';
import { TicketListHeader } from '../components/TicketListHeader';
import { TicketsScreenNavigationProp } from '../models/Navigation';

interface Props {
  tickets: Ticket[];
  navigation: TicketsScreenNavigationProp;
}
export const TicketList = ({ tickets, navigation }: Props) => {
  const renderItem = ({ item }: { item: Ticket }) => {
    return (
      <Pressable
        onPress={() => {
          navigation.navigate('Ticket', { ticket: item });
        }}
      >
        <TicketRow ticket={item} />
      </Pressable>
    );
  };
  return (
    <FlatList
      data={tickets}
      renderItem={renderItem}
      keyExtractor={(ticket: Ticket) => ticket.id.toString()}
      ListHeaderComponent={TicketListHeader}
    />
  );
};
