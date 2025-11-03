
import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import sampleMeals from '../data/sampleMeals.json';

function RecommendationItem({rec}) {
  return (
    <View style={{padding:10, borderBottomWidth:1, borderColor:'#eee'}}>
      <Text style={{fontWeight:'600'}}>{rec.title}</Text>
      <Text>{rec.description}</Text>
    </View>
  );
}

export default function RecommendationScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Diet Recommendations</Text>
      <FlatList
        data={sampleMeals.recommendations}
        keyExtractor={(item) => item.id}
        renderItem={({item}) => <RecommendationItem rec={item} />}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container:{flex:1,padding:16},
  title:{fontSize:20,fontWeight:'bold',marginBottom:8}
});
