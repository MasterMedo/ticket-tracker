import { StackNavigationProp } from '@react-navigation/stack';
import { RouteProp } from '@react-navigation/native';
import { Ticket } from '../models/Ticket';

export type NavigationParamList = {
  Tickets: {};
  Ticket: { ticket: Ticket };
  TicketCreate: { submitter_id: number };
};

export type TicketScreenNavigationProp = StackNavigationProp<
  NavigationParamList,
  'Ticket'
>;
export type TicketsScreenNavigationProp = StackNavigationProp<
  NavigationParamList,
  'Tickets'
>;
export type TicketCreateScreenNavigationProp = StackNavigationProp<
  NavigationParamList,
  'TicketCreate'
>;

export type TicketScreenRouteProp = RouteProp<NavigationParamList, 'Ticket'>;
export type TicketsScreenRouteProp = RouteProp<NavigationParamList, 'Ticket'>;
export type TicketCreateScreenRouteProp = RouteProp<
  NavigationParamList,
  'TicketCreate'
>;
