import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-giocatori',
  imports: [CommonModule],
  templateUrl: './giocatori.html',
  styleUrl: './giocatori.css'
})
export class Giocatori {
   data!: Object; //Il ‘!’ serve a creare variabili non inizializzate
   loading: boolean=false;
   o! :Observable<Object>;
   players = ['Mateo Retegui', 'Moise Kean', 'Ademola Lookman', 'Riccardo Orsolini', 'Marcus Thuram', 'Romelu Lukaku', 'Lautaro Martinez', 'Scott McTominay', 'Artem Dovbyk', 'Lorenzo Lucca', 'Nikola Krstovic', 'Christian Pulisic', 'Roberto Piccoli', 'Andrea Pinamonti', 'Dusan Vlahovic', 'Taty Castellanos', 'Pedro', 'Tijjani Reijnders', 'Boulaye Dia', 'Ché Adams'];
   constructor(public http: HttpClient) {}
   makeRequest(): void {
     console.log("here");
     this.loading = true;
     this.o = this.http.get('https://special-memory-jjrrpvp6gw992pjgq-5000.app.github.dev/players');
     this.o.subscribe(this.getData);
   }
   getData = (d : Object) =>
   {
     this.data = new Object(d);
     this.loading = false;
   }

}
