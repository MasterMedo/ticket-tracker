import React, { useEffect, useState } from 'react';
import { Pressable, View, Text, TextInput, StyleSheet } from 'react-native';
import {
  TicketCreateScreenNavigationProp,
  TicketCreateScreenRouteProp,
} from '../models/Navigation';
import { server } from '../config';
import { Category } from '../models/Category';
import { Ticket } from '../models/Ticket';

interface Props {
  navigation: TicketCreateScreenNavigationProp;
  route: TicketCreateScreenRouteProp;
}

export const TicketCreateScreen = ({ navigation }: Props) => {
  const [title, setTitle] = useState<string>();
  const [content, setContent] = useState<string>();
  const [category, setCategory] = useState<number>();
  const [categories, setCategories] = useState<Category[]>();
  const createTicket = () => {
    if (!!title && !!content && category) {
      fetch(server + '/tickets', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: title,
          content: content,
          category_id: category,
        }),
      })
        .then((r) => {
          if (r.ok) {
            return r.json();
          } else {
            throw new Error("couldn't add ticket");
          }
        })
        .then((ticket: Ticket) => {
          navigation.navigate('Ticket', { ticket });
        });
    }
  };
  useEffect(() => {
    fetch(server + '/categories')
      .then((r) => r.json())
      .then((data: Category[]) => {
        setCategories(data);
        if (data.length > 0) {
          setCategory(data[0].id);
        }
      })
      .catch((error) => console.warn(error));
  }, []);
  return (
    <View>
      <View style={styles.container}>
        <TextInput
          style={styles.title}
          placeholder="Title"
          onChangeText={(text) => setTitle(text)}
        />
        <TextInput
          style={styles.text}
          placeholder="What seems to be the issue?"
          onChangeText={(text) => setContent(text)}
        />
      </View>
      <Pressable onPress={createTicket} style={styles.submit}>
        <Text style={styles.text}>Submit</Text>
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#ffffff',
    padding: 10,
    marginVertical: 10,
    marginHorizontal: 10,
    borderRadius: 10,
  },
  title: {
    fontSize: 25,
  },
  text: {
    fontSize: 18,
  },
  submit: {
    backgroundColor: '#ffffff',
    padding: 10,
    marginVertical: 10,
    marginHorizontal: 10,
    borderRadius: 10,
  },
});
