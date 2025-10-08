import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Giocatori } from './giocatori/giocatori';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Giocatori],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('lavoro');
}
