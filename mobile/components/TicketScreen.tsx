import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import {
  TicketScreenNavigationProp,
  TicketScreenRouteProp,
} from '../models/Navigation';

interface Props {
  route: TicketScreenRouteProp;
  navigation: TicketScreenNavigationProp;
}

export const TicketScreen = ({ route }: Props) => {
  const { ticket } = route.params;
  if (!ticket) {
    return <></>;
  }
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{ticket.title}</Text>
      <Text style={styles.content}>{ticket.content}</Text>
      <Text style={styles.small}>{ticket.submitter_id}</Text>
      <Text style={styles.small}>{ticket.timestamp}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#ffffff',
    borderRadius: 15,
    marginHorizontal: 10,
    marginVertical: 10,
    padding: 10,
  },
  title: {
    fontSize: 25,
  },
  content: {
    fontSize: 18,
  },
  small: {
    fontSize: 16,
  },
});
